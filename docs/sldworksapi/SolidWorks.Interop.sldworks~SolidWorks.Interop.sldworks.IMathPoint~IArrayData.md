# IArrayData Property (IMathPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IArrayData`

Gets or sets the array of x,y,z coordinates that describe this math point.
Gets or sets the array of x,y,z coordinates that describe this math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IArrayData As System.Double
```

```

Dim instance As IMathPoint
Dim value As System.Double
 
instance.IArrayData = value
 
value = instance.IArrayData
```

```

System.double IArrayData {get; set;}
```

```

property System.double IArrayData {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles representing the x,y,z coordinates of the math point

- VBA, VB.NET, C#, and C++/CLI: Not supported

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::ArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ArrayData.md)
