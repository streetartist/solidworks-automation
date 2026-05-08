# UseAutoRelief Property (ISheetMetalFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseAutoRelief`

Gets or sets whether this sheet metal feature uses auto relief.
Gets or sets whether this sheet metal feature uses auto relief.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseAutoRelief As System.Boolean
```

```

Dim instance As ISheetMetalFeatureData
Dim value As System.Boolean
 
instance.UseAutoRelief = value
 
value = instance.UseAutoRelief
```

```

System.bool UseAutoRelief {get; set;}
```

```

property System.bool UseAutoRelief {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use auto relief, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)  
[ISheetMetalFeatureData::AutoReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AutoReliefType.md)  
[ISheetMetalFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~ReliefRatio.md)
