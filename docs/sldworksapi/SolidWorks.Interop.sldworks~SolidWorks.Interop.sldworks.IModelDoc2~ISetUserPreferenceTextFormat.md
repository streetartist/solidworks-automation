# ISetUserPreferenceTextFormat Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetUserPreferenceTextFormat`

Obsolete. Superseded by IModelDocExtension::SetUserPreferenceTextFormat.
Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As TextFormat _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim Value As TextFormat
Dim value As System.Boolean
 
value = instance.ISetUserPreferenceTextFormat(UserPreferenceValue, Value)
```

```

System.bool ISetUserPreferenceTextFormat( 
   System.int UserPreferenceValue,
   TextFormat Value
)
```

```

System.bool ISetUserPreferenceTextFormat( 
   System.int UserPreferenceValue,
   TextFormat^ Value
) 
```

#### Parameters

*UserPreferenceValue*
:   User preference to change as defined in [swUserPreferenceTextFormat\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceTextFormat_e.html)

*Value*
:   Text format to which to assign the user preference specified in UserPreferenceValue

#### Return Value

True if the setting is changed successfully, false if not

Remarks

This method is

- intended for setting detailing text formats.
- equivalent to interactively setting document options in the SOLIDWORKS software.

See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
