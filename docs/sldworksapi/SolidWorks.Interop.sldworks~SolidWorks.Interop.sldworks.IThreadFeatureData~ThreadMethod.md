# ThreadMethod Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ThreadMethod`

Gets or sets the thread method for this thread feature.
Gets or sets the thread method for this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThreadMethod As System.Integer
```

```

Dim instance As IThreadFeatureData
Dim value As System.Integer
 
instance.ThreadMethod = value
 
value = instance.ThreadMethod
```

```

System.int ThreadMethod {get; set;}
```

```

property System.int ThreadMethod {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thread method as defined in [swThreadMethod\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadMethod_e.html); default is swThreadMethod\_e.swThreadMethod\_CutThread

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
