# SetSelections2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2`

Sets the selected objects for the macro feature.
Sets the selected objects for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSelections2( _
   ByVal Objects As System.Object, _
   ByVal SelMarks As System.Object, _
   ByVal DrViews As System.Object _
) 
```

```

Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim SelMarks As System.Object
Dim DrViews As System.Object
 
instance.SetSelections2(Objects, SelMarks, DrViews)
```

```

void SetSelections2( 
   System.object Objects,
   System.object SelMarks,
   System.object DrViews
)
```

```

void SetSelections2( 
   System.Object^ Objects,
   System.Object^ SelMarks,
   System.Object^ DrViews
) 
```

#### Parameters

*Objects*
:   Array of objects as defined in  [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) to select (see **Remarks**)

*SelMarks*
:   Array of selection marks (integers or longs) for the objects (see **Remarks**)

*DrViews*
:   Array of [drawing views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) (see **Remarks**)

Remarks

Early bind the Objects, SelMarks, and DrViews arrays when declaring them to avoid possible problems when using other IMacroFeatureData methods.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetSelectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.md)  
[IMacroFeatureData::GetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md)  
[IMacroFeatureData::IGetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md)  
[IMacroFeatureData::ISetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.md)
