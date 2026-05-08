# EnablePartialEdgeParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters`

Gets or sets whether to enable partial edge properties for all edges of this fillet.
Gets or sets whether to enable partial edge properties for all edges of this fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnablePartialEdgeParameters As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean
 
instance.EnablePartialEdgeParameters = value
 
value = instance.EnablePartialEdgeParameters
```

```

System.bool EnablePartialEdgeParameters {get; set;}
```

```

property System.bool EnablePartialEdgeParameters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable partial edge properties for all edges, false to not

Example

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
