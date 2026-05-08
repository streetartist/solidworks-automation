# NetworkRendering Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering`

Gets or sets whether to enable network rendering.
Gets or sets whether to enable network rendering.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NetworkRendering As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.NetworkRendering = value
 
value = instance.NetworkRendering
```

```

System.bool NetworkRendering {get; set;}
```

```

property System.bool NetworkRendering {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable network rendering, false to not

Remarks

Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::ClientWorkload Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.md)  
[IRayTraceRendererOptions::NetworkSharedDirectory Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.md)  
[IRayTraceRendererOptions::SendDataForNetworkJob Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.md)  
[IRayTraceRendererOptions:OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.md)
