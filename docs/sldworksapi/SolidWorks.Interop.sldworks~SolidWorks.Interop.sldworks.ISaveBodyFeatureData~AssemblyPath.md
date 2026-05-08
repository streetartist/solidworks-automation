# AssemblyPath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AssemblyPath`

Gets or sets the path and filename of the assembly (*.sldasm) of save bodies.
Gets or sets the path and filename of the assembly (\*.**sldasm**) of save bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AssemblyPath As System.String
```

```

Dim instance As ISaveBodyFeatureData
Dim value As System.String
 
instance.AssemblyPath = value
 
value = instance.AssemblyPath
```

```

System.string AssemblyPath {get; set;}
```

```

property System.String^ AssemblyPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and filename of the assembly (\*.**sldasm**) of save bodies

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)  
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.md)
