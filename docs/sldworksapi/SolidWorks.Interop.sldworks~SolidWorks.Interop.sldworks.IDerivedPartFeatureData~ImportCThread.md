# ImportCThread Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCThread`

Gets or sets whether to import cosmetic threads with the derived part feature.
Gets or sets whether to import [cosmetic threads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md) with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportCThread As System.Boolean
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean
 
instance.ImportCThread = value
 
value = instance.ImportCThread
```

```

System.bool ImportCThread {get; set;}
```

```

property System.bool ImportCThread {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import its cosmetics threads, false not not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
