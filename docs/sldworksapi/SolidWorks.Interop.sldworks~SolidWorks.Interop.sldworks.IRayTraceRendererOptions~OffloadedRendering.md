# OffloadedRendering Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering`

Gets or sets whether to offload rendering to other networked machines.
Gets or sets whether to offload rendering to other networked machines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffloadedRendering As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.OffloadedRendering = value
 
value = instance.OffloadedRendering
```

```

System.bool OffloadedRendering {get; set;}
```

```

property System.bool OffloadedRendering {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to offload rendering, false to not

Remarks

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions:ClientWorkload Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.md)  
[IRayTraceRendererOptions:NetworkRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.md)  
[IRayTraceRendererOptions:NetworkSharedDirectory Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.md)  
[IRayTraceRendererOptions:SendDataForNetworkJob Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.md)
