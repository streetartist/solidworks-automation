# LightSourceUserName Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LightSourceUserName`

Obsolete. Superseded by IModelDoc2::LightSourceUserName.
Obsolete. Superseded by [IModelDoc2::LightSourceUserName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LightSourceUserName( _
   ByVal ID As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.String
 
instance.LightSourceUserName(ID) = value
 
value = instance.LightSourceUserName(ID)
```

```

System.string LightSourceUserName( 
   System.int ID
) {get; set;}
```

```

property System.String^ LightSourceUserName {
   System.String^ get(System.int ID);
   void set (System.int ID, System.String^ value);
}
```

#### Parameters

*ID*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
