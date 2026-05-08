# IArrayData Property (IMathVector)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IArrayData`

Gets or sets the array of three doubles for this vector.
Gets or sets the array of three doubles for this vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IArrayData As System.Double
```

```

Dim instance As IMathVector
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

- in-process, unmanaged C++: Pointerto an array of three doubles

- VBA, VB.NET, C#, and C++/CLI: Not supported

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::ArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ArrayData.md)
