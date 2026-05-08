# GetUserPreferenceToggle Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceToggle`

Obsolete. Superseded by IModelDocExtension::GetUserPreferenceToggle.
Obsolete. Superseded by [IModelDocExtension::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPreferenceToggle( _
   ByVal UserPreferenceToggle As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim UserPreferenceToggle As System.Integer
Dim value As System.Boolean
 
value = instance.GetUserPreferenceToggle(UserPreferenceToggle)
```

```

System.bool GetUserPreferenceToggle( 
   System.int UserPreferenceToggle
)
```

```

System.bool GetUserPreferenceToggle( 
   System.int UserPreferenceToggle
) 
```

#### Parameters

*UserPreferenceToggle*
:   Value as defined in [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html)

#### Return Value

True if the item specified by UserPreferenceToggle is currently toggled on, false if the item is currently toggled off

Remarks

This method is equivalent to interactively getting document properties in the SOLIDWORKS product.

The value returned is true if the item is currently turned on, and false if the item is currently turned off. For example:

> boolean curState = m\_ModelDoc2.GetUserPreferenceToggle( swIgnoreFeatureColors )

See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Example

[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)  
[Ignore Feature Colors (VBA)](Ignore_Feature_Colors_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
