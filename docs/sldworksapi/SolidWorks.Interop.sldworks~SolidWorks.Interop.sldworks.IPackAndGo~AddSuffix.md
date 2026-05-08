# AddSuffix Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddSuffix`

Gets or sets a suffix for all filenames for Pack and Go.
Gets or sets a suffix for all filenames for Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddSuffix As System.String
```

```

Dim instance As IPackAndGo
Dim value As System.String
 
instance.AddSuffix = value
 
value = instance.AddSuffix
```

```

System.string AddSuffix {get; set;}
```

```

property System.String^ AddSuffix {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Suffix for all filenames

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
[IPackAndGo::AddPrefix Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddPrefix.md)  
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md)  
[IPackAndGo::SetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md)  
[IPackAndGo::SetSaveToName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md)
