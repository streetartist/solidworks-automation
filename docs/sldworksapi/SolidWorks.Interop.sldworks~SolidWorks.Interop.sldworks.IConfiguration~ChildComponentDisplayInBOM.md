# ChildComponentDisplayInBOM Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM`

Gets or sets the child component display option of this configuration in the Bill of Materials (BOM) for an assembly or for a cutlist part (weldment and/or sheet metal).
Gets or sets the child component display option of this configuration in the Bill of Materials (BOM) for an assembly or for a cutlist part (weldment and/or sheet metal).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ChildComponentDisplayInBOM As System.Integer
```

```

Dim instance As IConfiguration
Dim value As System.Integer
 
instance.ChildComponentDisplayInBOM = value
 
value = instance.ChildComponentDisplayInBOM
```

```

System.int ChildComponentDisplayInBOM {get; set;}
```

```

property System.int ChildComponentDisplayInBOM {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Child component display option as defined in [swChildComponentInBOMOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChildComponentInBOMOption_e.html)

Example

[Add Configuration and Promote Child Components in BOM (C#)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_CSharp.htm)  
[Add Configuration and Promote Child Components in BOM (VB.NET)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VBNET.htm)  
[Add Configuration and Promote Child Components in BOM (VBA)](Add_Configuration_and_Promote_Child_Components_in_BOM_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IModelDoc2::AddConfiguration3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)
