# ArrayData Property (IMathVector)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ArrayData`

Gets or sets the array of three doubles for this vector.
Gets or sets the array of three doubles for this vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ArrayData As System.Object
```

```

Dim instance As IMathVector
Dim value As System.Object
 
instance.ArrayData = value
 
value = instance.ArrayData
```

```

System.object ArrayData {get; set;}
```

```

property System.Object^ ArrayData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of three doubles

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::IArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IArrayData.md)
