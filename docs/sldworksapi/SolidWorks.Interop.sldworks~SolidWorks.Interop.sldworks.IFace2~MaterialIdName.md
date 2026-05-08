# MaterialIdName Property (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialIdName`

Gets or sets the material name.
Gets or sets the material name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaterialIdName As System.String
```

```

Dim instance As IFace2
Dim value As System.String
 
instance.MaterialIdName = value
 
value = instance.MaterialIdName
```

```

System.string MaterialIdName {get; set;}
```

```

property System.String^ MaterialIdName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Material name

Remarks

This property is unsupported for faces obtained from reference surface bodies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IModelDoc2::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialIdName.md)  
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.md)  
[IFace2::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.md)
