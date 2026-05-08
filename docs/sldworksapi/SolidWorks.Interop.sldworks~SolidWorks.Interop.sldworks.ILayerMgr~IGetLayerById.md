# IGetLayerById Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById`

Gets the layer using the specified layer ID in this drawing document.
Gets the layer using the specified layer ID in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLayerById( _
   ByVal LayerId As System.Short _
) As Layer
```

```

Dim instance As ILayerMgr
Dim LayerId As System.Short
Dim value As Layer
 
value = instance.IGetLayerById(LayerId)
```

```

Layer IGetLayerById( 
   System.short LayerId
)
```

```

Layer^ IGetLayerById( 
   System.short LayerId
) 
```

#### Parameters

*LayerId*
:   Layer ID

#### Return Value

[ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object

Remarks

You can get the layer ID from several places. [IView::IGetUserPoints2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetUserPoints2.md) and [IView::IGetLines4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetLines4.md) (and similar functions) return the LayerId as part of the array of return information. [IAnnotation::IGetVisualProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetVisualProperties.md) also returns the LayerId as part of the array of return information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[ILayerMgr::GetLayerById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md)
