# ClientWorkload Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload`

Gets or sets how many buckets (sections of rendering) are sent to each client processor.
Gets or sets how many buckets (sections of rendering) are sent to each client processor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ClientWorkload As System.Integer
```

```

Dim instance As IRayTraceRendererOptions
Dim value As System.Integer
 
instance.ClientWorkload = value
 
value = instance.ClientWorkload
```

```

System.int ClientWorkload {get; set;}
```

```

property System.int ClientWorkload {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of buckets sent to each client processor (see **Remarks**)

Remarks

A high client workload setting is appropriate if the client machines are more powerful than the coordinator machine.

Using a [shared network directory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.md) for [network renders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.md):

- can be faster when using many client machines.
- avoids having to [send scene asset data to each node on the network](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.md).

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.md)  
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.md)  
[IRayTraceRendererOptions::OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.md)
