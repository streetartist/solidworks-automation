# SetUserPreferenceStringValue Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceStringValue`

Obsolete. Superseded by IModelDocExtension::SetUserPreferenceString.
Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim UserPreference As System.Integer
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.SetUserPreferenceStringValue(UserPreference, Value)
```

```

System.bool SetUserPreferenceStringValue( 
   System.int UserPreference,
   System.string Value
)
```

```

System.bool SetUserPreferenceStringValue( 
   System.int UserPreference,
   System.String^ Value
) 
```

#### Parameters

*UserPreference*
:   User preference value as defined in [swUserPreferenceStringValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceStringValue_e.html)

*Value*
:   Value of the user preference specified in UserPreference

#### Return Value

True if user preference value is changed, false if not

Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
