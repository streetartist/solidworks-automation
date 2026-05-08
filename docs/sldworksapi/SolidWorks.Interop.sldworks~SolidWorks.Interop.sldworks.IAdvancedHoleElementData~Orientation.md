# Orientation Property (IAdvancedHoleElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~Orientation`

Gets or sets the orientation of this Advanced Hole element.
Gets or sets the orientation of this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Orientation As System.Integer
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.Integer
 
instance.Orientation = value
 
value = instance.Orientation
```

```

System.int Orientation {get; set;}
```

```

property System.int Orientation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Orientation as defined in [swHoleElementOrientation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHoleElementOrientation_e.html) (see **Remarks**)

Remarks

This property is not valid if [IAdvancedHoleElementData::ElementType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~ElementType.md) is set to [swAdvWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvWzdGeneralHoleTypes_e.html):

- swAdvWzdStraight
- swAdvWzdStraightTap

Example

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)
