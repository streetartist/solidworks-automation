# IArrayData Property (IMathTransform)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IArrayData`

Gets and sets the array of 16 doubles for this transform.
Gets and sets the array of 16 doubles for this transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IArrayData As System.Double
```

```

Dim instance As IMathTransform
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

- in-process, unmanaged C++: Pointer to an array of 16 doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

Remarks

The first 9 elements define the 3x3 rotation matrix. The next 3 elements define the translation component. The next element defines the scaling component. The last 3 elements are unused.

The array data argument should be in a form that allows the direct calling of methods such as [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)  
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)
