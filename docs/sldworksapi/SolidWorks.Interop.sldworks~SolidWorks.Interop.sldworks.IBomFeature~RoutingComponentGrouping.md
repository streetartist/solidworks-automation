# RoutingComponentGrouping Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~RoutingComponentGrouping`

Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components.
Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RoutingComponentGrouping As System.Integer
```

```

Dim instance As IBomFeature
Dim value As System.Integer
 
instance.RoutingComponentGrouping = value
 
value = instance.RoutingComponentGrouping
```

```

System.int RoutingComponentGrouping {get; set;}
```

```

property System.int RoutingComponentGrouping {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Routing component grouping options as defined in [swRoutingComponentGroupOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRoutingComponentGroupingOption_e.html)

Example

[Get and Set Routing Component Grouping Options for BOM Table (C#)](Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_CSharp.htm)  
[Get and Set Routing Component Grouping Options for BOM Table (VB.NET)](Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_VBNET.htm)  
[Get and Set Routing Component Grouping Options for BOM Table (VBA)](Get_and_Set_Routing_Component_Grouping_Options_for_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)
