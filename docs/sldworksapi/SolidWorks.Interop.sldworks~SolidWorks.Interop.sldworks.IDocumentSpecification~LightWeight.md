# LightWeight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LightWeight`

Gets or sets whether to open an assembly or drawing document with lightweight parts.
Gets or sets whether to open an assembly or drawing document with lightweight parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LightWeight As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.LightWeight = value
 
value = instance.LightWeight
```

```

System.bool LightWeight {get; set;}
```

```

property System.bool LightWeight {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to open the assembly or drawing document with lightweight parts, false to not

Remarks

[IDocumentSpecification::UseLightWeightDefault](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~UseLightWeightDefault.md) must be false for this property to have an effect.

Example

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)  
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)  
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)  
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
