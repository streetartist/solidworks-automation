# SendDataForNetworkJob Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob`

Gets or sets whether to send rendering data over the network.
Gets or sets whether to send rendering data over the network.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SendDataForNetworkJob As System.Boolean
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean
 
instance.SendDataForNetworkJob = value
 
value = instance.SendDataForNetworkJob
```

```

System.bool SendDataForNetworkJob {get; set;}
```

```

property System.bool SendDataForNetworkJob {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to send rendering data over the network, false to not

Remarks

Use this property to send rendering data over the network instead of using a [shared network directory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.md).

Sending rendering data over the network avoids issues with permissions and cross-platform configurations that might occur when using a shared network directory.

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::ClientWorkload Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.md)  
[IRayTraceRendererOptions::NetworkRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.md)  
[IRayTraceRendererOptions:OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.md)
