# LightSourcePropertyValues Property (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LightSourcePropertyValues`

Obsolete. Superseded by IModelDoc2::LightSourcePropertyValues.
Obsolete. Superseded by [IModelDoc2::LightSourcePropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LightSourcePropertyValues( _
   ByVal ID As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.Object
 
instance.LightSourcePropertyValues(ID) = value
 
value = instance.LightSourcePropertyValues(ID)
```

```

System.object LightSourcePropertyValues( 
   System.int ID
) {get; set;}
```

```

property System.Object^ LightSourcePropertyValues {
   System.Object^ get(System.int ID);
   void set (System.int ID, System.Object^ value);
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
