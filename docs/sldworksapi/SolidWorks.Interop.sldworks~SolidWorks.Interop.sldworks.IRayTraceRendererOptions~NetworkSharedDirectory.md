# NetworkSharedDirectory Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory`

Gets or sets the name of the shared network directory for network renders.
Gets or sets the name of the shared network directory for [network renders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NetworkSharedDirectory As System.String
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.String
 
instance.NetworkSharedDirectory = value
 
value = instance.NetworkSharedDirectory
```

```

System.string NetworkSharedDirectory {get; set;}
```

```

property System.String^ NetworkSharedDirectory {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the shared network directory for network renders

Remarks

Using a shared network directory for network renders:

- avoids having to [send scene asset data to each node on the network](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.md).
- can be faster when using many [client machines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.md).

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions:OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.md)
