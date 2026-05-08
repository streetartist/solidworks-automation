# ReferencedDocument Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument`

Gets the document referenced by this drawing view.
Gets the document referenced by this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferencedDocument As ModelDoc2
```

```

Dim instance As IView
Dim value As ModelDoc2
 
value = instance.ReferencedDocument
```

```

ModelDoc2 ReferencedDocument {get;}
```

```

property ModelDoc2^ ReferencedDocument {
   ModelDoc2^ get();
}
```

#### Property Value

[Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

Because section views do not have referenced documents, this method returns an empty string for this type of view. Instead, use [IView::GetBaseView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.md) or [IView::IGetBaseView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.md) to get the parent view of a section, and then get its referenced document from that view.

Example

[Get Document Referenced by Drawing View (VBA)](Get_Document_Referenced_by_Drawing_View_Example_VB.htm)  
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)  
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)  
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::ReferencedConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration.md)  
[IView::GetReferencedModelName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName.md)  
[IView::ReferencedConfigurationID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.md)
