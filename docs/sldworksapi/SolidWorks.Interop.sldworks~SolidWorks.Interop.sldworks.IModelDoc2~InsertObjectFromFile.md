# InsertObjectFromFile Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertObjectFromFile`

Obsolete. Superseded by IModelDocExtension::InsertObjectFromFile.
Obsolete. Superseded by [IModelDocExtension::InsertObjectFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertObjectFromFile( _
   ByVal FilePath As System.String, _
   ByVal CreateLink As System.Boolean, _
   ByVal Xx As System.Double, _
   ByVal Yy As System.Double, _
   ByVal Zz As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FilePath As System.String
Dim CreateLink As System.Boolean
Dim Xx As System.Double
Dim Yy As System.Double
Dim Zz As System.Double
Dim value As System.Boolean
 
value = instance.InsertObjectFromFile(FilePath, CreateLink, Xx, Yy, Zz)
```

```

System.bool InsertObjectFromFile( 
   System.string FilePath,
   System.bool CreateLink,
   System.double Xx,
   System.double Yy,
   System.double Zz
)
```

```

System.bool InsertObjectFromFile( 
   System.String^ FilePath,
   System.bool CreateLink,
   System.double Xx,
   System.double Yy,
   System.double Zz
) 
```

#### Parameters

*FilePath*

*CreateLink*

*Xx*

*Yy*

*Zz*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
