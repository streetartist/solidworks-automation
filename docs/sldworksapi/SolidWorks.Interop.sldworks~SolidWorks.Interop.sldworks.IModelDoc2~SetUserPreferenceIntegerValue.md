# SetUserPreferenceIntegerValue Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceIntegerValue`

Obsolete. Superseded by IModelDocExtension::SetUserPreferenceInteger.
Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean
 
value = instance.SetUserPreferenceIntegerValue(UserPreferenceValue, Value)
```

```

System.bool SetUserPreferenceIntegerValue( 
   System.int UserPreferenceValue,
   System.int Value
)
```

```

System.bool SetUserPreferenceIntegerValue( 
   System.int UserPreferenceValue,
   System.int Value
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference value as defined in [swUserPreferenceIntegerValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)

*Value*
:   Numeric value you give to the user preference specified in UserPreferenceValue

#### Return Value

True if the setting is changed successfully, false if not

Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Example

[Set Grid Lines (VBA)](Set_Grid_Lines_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
