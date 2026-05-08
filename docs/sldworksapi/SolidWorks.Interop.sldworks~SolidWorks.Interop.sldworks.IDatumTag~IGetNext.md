# IGetNext Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetNext`

Gets the next datum tag in the view.
Gets the next datum tag in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNext() As DatumTag
```

```

Dim instance As IDatumTag
Dim value As DatumTag
 
value = instance.IGetNext()
```

```

DatumTag IGetNext()
```

```

DatumTag^ IGetNext(); 
```

#### Return Value

Pointer to the next [datum tag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatum::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetNext.md)  
[IView::GetFirstDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTag.md)  
[IView::IGetFirstDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDatumTag.md)  
[IModelDoc2::IInsertDatumTag2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertDatumTag2.md)  
[IModelDoc2::InsertDatumTag2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDatumTag2.md)  
[IAnnotation::GetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.md)  
[IAnnotation::IGetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.md)
