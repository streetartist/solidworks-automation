# SetCurrentLayer Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetCurrentLayer`

Sets the current layer used by this document.
Sets the current layer used by this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCurrentLayer( _
   ByVal Layername As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Layername As System.String
Dim value As System.Boolean
 
value = instance.SetCurrentLayer(Layername)
```

```

System.bool SetCurrentLayer( 
   System.string Layername
)
```

```

System.bool SetCurrentLayer( 
   System.String^ Layername
) 
```

#### Parameters

*Layername*
:   Name of the layer

Remarks

SOLIDWORKS creates subsequent items on the specified layer.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ChangeComponentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeComponentLayer.md)  
[IDrawingDoc::CreateLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLayer.md)  
[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)
