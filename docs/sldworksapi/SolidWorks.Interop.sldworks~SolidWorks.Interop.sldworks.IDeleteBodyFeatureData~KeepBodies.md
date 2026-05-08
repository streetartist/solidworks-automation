# KeepBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~KeepBodies`

Gets or sets whether to keep bodies.
Gets or sets whether to keep bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepBodies As System.Boolean
```

```

Dim instance As IDeleteBodyFeatureData
Dim value As System.Boolean
 
instance.KeepBodies = value
 
value = instance.KeepBodies
```

```

System.bool KeepBodies {get; set;}
```

```

property System.bool KeepBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep bodies, false to delete bodies

Remarks

Call [IDeleteBodyFeatureData::Bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.md) to specify the bodies to keep or delete.

Example

See the [IDeleteBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md)  
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.md)
