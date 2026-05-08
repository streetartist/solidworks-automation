# GetModelViewCount Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViewCount`

Gets the number of model views in this document.
Gets the number of model views in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelViewCount() As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
value = instance.GetModelViewCount()
```

```

System.int GetModelViewCount()
```

```

System.int GetModelViewCount(); 
```

#### Return Value

Number of model views

Remarks

Call this method before calling [IModelDocExtension::IGetModelViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetModelViews.md) to determine the size of the array for that method.

Example

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)  
[Get Scale Factor of Each Model View (C#)](Get_Scale_of_Each_Model_View_Example_CSharp.htm)  
[Get Scale Factor of Each Model View (VB.NET)](Get_Scale_of_Each_Model_View_Example_VBNET.htm)  
[Get Scale Factor of Each Model View (VBA)](Get_Scale_of_Each_Model_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelViews.md)  
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.md)  
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.md)  
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.md)  
[IModelView::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.md)
