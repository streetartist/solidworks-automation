# GetRayTraceRenderer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRayTraceRenderer`

Get a ray-trace rendering engine.
Get a ray-trace rendering engine.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRayTraceRenderer( _
   ByVal RendererType As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim RendererType As System.Integer
Dim value As System.Object
 
value = instance.GetRayTraceRenderer(RendererType)
```

```

System.object GetRayTraceRenderer( 
   System.int RendererType
)
```

```

System.Object^ GetRayTraceRenderer( 
   System.int RendererType
) 
```

#### Parameters

*RendererType*
:   Type of ray-trace rendering engine as defined in [swRayTraceRenderType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderType_e.html)

#### Return Value

[Ray trace renderer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.md)

Example

[Render Model (C#)](Render_Model_Example_CSharp.htm)  
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)  
[Render Model (VBA)](Render_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetRayTraceRenderer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetRayTraceRenderer.md)
