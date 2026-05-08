# DefinedBy Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DefinedBy`

Gets or sets the definition of this helix feature.
Gets or sets the definition of this helix feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DefinedBy As System.Integer
```

```

Dim instance As IHelixFeatureData
Dim value As System.Integer
 
instance.DefinedBy = value
 
value = instance.DefinedBy
```

```

System.int DefinedBy {get; set;}
```

```

property System.int DefinedBy {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of helix as defined by [swHelixDefinedBy\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHelixDefinedBy_e.html)

Example

[Create or Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)  
[Create or Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)  
[Create or Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)
