# FlipDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~FlipDirection`

Gets or sets whether to change the endpoint from where to measure distance.
Gets or sets whether to change the endpoint from where to measure distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipDirection As System.Boolean
```

```

Dim instance As ISlotMateFeatureData
Dim value As System.Boolean
 
instance.FlipDirection = value
 
value = instance.FlipDirection
```

```

System.bool FlipDirection {get; set;}
```

```

property System.bool FlipDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to change the endpoint, false to  not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.md)  
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.md)  
[ISlotMateFeatureData::Distance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Distance.md)  
[ISlotMateFeatureData::Percent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Percent.md)
