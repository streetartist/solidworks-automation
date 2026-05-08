# SetUserPreferenceToggle Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle`

Obsolete. Superseded by IModelDocExtension::SetUserPreferenceToggle.
Obsolete. Superseded by [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.SetUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

```

System.bool SetUserPreferenceToggle( 
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

```

System.bool SetUserPreferenceToggle( 
   System.int UserPreferenceValue,
   System.bool OnFlag
) 
```

#### Parameters

*UserPreferenceValue*
:   Value to toggle as defined in [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html)

*OnFlag*
:   True to toggle the value on, false to toggle the value off

#### Return Value

True if the toggle is successful, false if not

Remarks

This method is equivalent to interactively setting document properties in the SOLIDWORKS software. See [System Options and Document Properties](sldworksapiprogguide.chm::/overview/System_Options_and_Document_Properties.htm) for details.

Example

[Hide or Show All Types (VBA)](Hide_or_Show_All_Types_Example_VB.htm)  
[Ignore Feature Colors (VBA)](Ignore_Feature_Colors_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
