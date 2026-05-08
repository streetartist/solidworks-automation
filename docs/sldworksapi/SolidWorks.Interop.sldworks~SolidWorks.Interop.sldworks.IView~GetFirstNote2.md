# GetFirstNote2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote2`

Gets the first note in the view.
Gets the first note in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstNote2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstNote2()
```

```

System.object GetFirstNote2()
```

```

System.Object^ GetFirstNote2(); 
```

#### Return Value

First [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

This method obsoletes IView::GetFirstNote by supporting inactive sheets.

The sheet must be visible. See [ISheet::SheetFormatVisible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md).

Example

[Change Note Text (VBA)](Change_Note_Text_Example_VB.htm)  
[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)  
[Select Silhouette Edge Attached to Note (VBA)](Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm)  
[Select Silhouette Edge Attached to Note (VB.NET)](Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm)  
[Select Silhouette Edge Attached to Note (C#)](Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[INote::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.md)
