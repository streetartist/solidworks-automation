# GetDatumTags Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTags`

Gets all of the datum tags on this drawing view.
Gets all of the datum tags on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumTags() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDatumTags()
```

```

System.object GetDatumTags()
```

```

System.Object^ GetDatumTags(); 
```

#### Return Value

Array of [datum tags](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)

Remarks

Use this method to obtain the array of datum tags all at once instead of calling [IView::GetFirstDatumTag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTag.md) and then repeatedly calling [IDatumTag::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetNext.md) to obtain the remaining datum tags on this drawing view.

Example

[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumTagCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTagCount.md)  
[IView::IGetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTags.md)
