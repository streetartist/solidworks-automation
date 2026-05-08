# EngageBelt Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~EngageBelt`

Gets and sets whether to engage the belt with the pulleys.
Gets and sets whether to engage the belt with the pulleys.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EngageBelt As System.Boolean
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Boolean
 
instance.EngageBelt = value
 
value = instance.EngageBelt
```

```

System.bool EngageBelt {get; set;}
```

```

property System.bool EngageBelt {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to engage the belt with the pulleys, false to suppress belt mates

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
