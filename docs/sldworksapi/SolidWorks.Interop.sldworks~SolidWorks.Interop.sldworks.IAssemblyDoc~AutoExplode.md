# AutoExplode Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoExplode`

Automatically generates an exploded view of the current assembly configuration.
Automatically generates an exploded view of the current assembly configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoExplode() As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
value = instance.AutoExplode()
```

```

System.bool AutoExplode()
```

```

System.bool AutoExplode(); 
```

#### Return Value

True if the exploded view is automatically generated, false if not

Remarks

This method creates only one exploded view per assembly configuration. To create multiple exploded views, use [IAssemblyDoc::CreateExplodedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateExplodedView.md).

It is difficult to get the exploded view perfect without some user interaction. However, this method makes an attempt based on the current mate conditions.

Example

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md) examples.

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Insert Explode Line Sketch and Route Line (VB.NET)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm)  
[Insert Explode Line Sketch and Route Line (VBA)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm)  
[Insert Explode Line Sketch and Route Line (C#)](Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewConfigurationName.md)  
[IAssemblyDoc::GetExplodedViewCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewCount2.md)  
[IAssemblyDoc::GetExplodedViewNames2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetExplodedViewNames2.md)  
[IAssemblyDoc::ShowExploded2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ShowExploded2.md)  
[IAssemblyDoc::ViewCollapseAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewCollapseAssembly.md)  
[IAssemblyDoc::ViewExplodeAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewExplodeAssembly.md)  
[IModelDocExtension::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsExploded.md)  
[ISketchManager::InsertExplodeLineSketch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.md)  
[IView::IsExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsExploded.md)  
[IView::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowExploded.md)  
[IConfiguration::AddRadialExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRadialExplodeStep.md)  
[IConfiguration::AddExplodeStep2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddExplodeStep2.md)
