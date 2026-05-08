# AddPrefix Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddPrefix`

Gets or sets a prefix for all filenames for Pack and Go.
Gets or sets a prefix for all filenames for Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddPrefix As System.String
```

```

Dim instance As IPackAndGo
Dim value As System.String
 
instance.AddPrefix = value
 
value = instance.AddPrefix
```

```

System.string AddPrefix {get; set;}
```

```

property System.String^ AddPrefix {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Prefix for all filenames

Example

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)  
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)  
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::AddSuffix Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddSuffix.md)  
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md)  
[IPackAndGo::SetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md)  
[IPackAndGo::SetSaveToName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md)
