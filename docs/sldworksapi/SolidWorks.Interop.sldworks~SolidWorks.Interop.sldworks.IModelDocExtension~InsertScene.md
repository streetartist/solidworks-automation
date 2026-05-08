# InsertScene Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertScene`

Applies the specified scene to the model.
Applies the specified scene to the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertScene( _
   ByVal SceneDefinitionFile As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim SceneDefinitionFile As System.String
Dim value As System.Boolean
 
value = instance.InsertScene(SceneDefinitionFile)
```

```

System.bool InsertScene( 
   System.string SceneDefinitionFile
)
```

```

System.bool InsertScene( 
   System.String^ SceneDefinitionFile
) 
```

#### Parameters

*SceneDefinitionFile*
:   Fully qualified path and filename for the scene

#### Return Value

True if the specified scene is displayed, false if not

Remarks

[RealView graphics must be enabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewDisplayRealView.md) to apply and view scenes.

Call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) or [IModelView::IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md) to repaint the graphics area.

Example

[Get Render References (C#)](Get_Render_References_Example_CSharp.htm)  
[Get Render References (VB.NET)](Get_Render_References_Example_VBNET.htm)  
[Get Render References (VBA)](Get_Render_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::DeleteScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteScene.md)  
[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.md)  
[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.md)  
[IConfiguration::GetScene Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetScene.md)
