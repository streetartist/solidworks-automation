# FastenerType Property (IAdvancedHoleElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType`

Gets or sets the fastener type for this Advanced Hole element.
Gets or sets the fastener type for this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FastenerType As System.Integer
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.Integer
 
instance.FastenerType = value
 
value = instance.FastenerType
```

```

System.int FastenerType {get; set;}
```

```

property System.int FastenerType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Hole fastener type as defined in [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

Remarks

The hole fastener must match the [IAdvancedHoleElementData::Standard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Standard.md) and be appropriate for the [IAdvancedHoleElementData::ElementType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.md), or an error occurs.

If [IAdvancedHoleElementData::ElementType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.md) is set to [swAdvWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html).swAdvWzdTaperTap, then this property gets and sets only swWzdHoleStandardFastenerTypes\_e.\*TaperedPipeTap.

Example

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)
