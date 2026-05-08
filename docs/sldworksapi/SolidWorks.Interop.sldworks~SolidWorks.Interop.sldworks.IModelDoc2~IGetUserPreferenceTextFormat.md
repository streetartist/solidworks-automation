# IGetUserPreferenceTextFormat Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserPreferenceTextFormat`

Obsolete. Superseded by IModelDocExtension::GetUserPreferenceTextFormat.
Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer _
) As TextFormat
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim value As TextFormat
 
value = instance.IGetUserPreferenceTextFormat(UserPreferenceValue)
```

```

TextFormat IGetUserPreferenceTextFormat( 
   System.int UserPreferenceValue
)
```

```

TextFormat^ IGetUserPreferenceTextFormat( 
   System.int UserPreferenceValue
) 
```

#### Parameters

*UserPreferenceValue*
:   Value as defined in [swUserPreferenceTextFormat\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceTextFormat_e.html)

#### Return Value

[Text format](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) associated with UserPreferenceValue

Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS product. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
