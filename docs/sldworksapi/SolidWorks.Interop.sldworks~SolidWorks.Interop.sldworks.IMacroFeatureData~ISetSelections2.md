# ISetSelections2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2`

Sets the selected objects for the macro feature.
Sets the selected objects for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSelections2( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef SelMarks As System.Integer, _
   ByRef DrViews As View _
) 
```

```

Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim SelMarks As System.Integer
Dim DrViews As View
 
instance.ISetSelections2(SelCount, Objects, SelMarks, DrViews)
```

```

void ISetSelections2( 
   System.int SelCount,
   ref System.object Objects,
   ref System.int SelMarks,
   ref View DrViews
)
```

```

void ISetSelections2( 
   System.int SelCount,
   System.Object^% Objects,
   System.int% SelMarks,
   View^% DrViews
) 
```

#### Parameters

*SelCount*
:   Number of selected objects

*Objects*
:   - in-process, unmanaged C++: Pointer to an array of objects as defined in  [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) of size SelCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*SelMarks*
:   - in-process, unmanaged C++: Pointer to an array of marks (integers or longs) of size SelCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*DrViews*
:   - in-process, unmanaged C++: Pointer to an array of [drawing views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) of size selCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The method expects to be passed three arrays of the same size.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md)  
[IMacroFeatureData::IGetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md)  
[IMacroFeatureData::SetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.md)  
[IMacroFeatureData::GetSelectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.md)
