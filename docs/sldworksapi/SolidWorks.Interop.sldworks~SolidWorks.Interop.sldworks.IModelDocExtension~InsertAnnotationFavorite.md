# InsertAnnotationFavorite Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAnnotationFavorite`

Inserts annotations from the specified favorite file at the specified location.
Inserts annotations from the specified favorite file at the specified location.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertAnnotationFavorite( _
   ByVal BstrFileName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Annotation
```

```

Dim instance As IModelDocExtension
Dim BstrFileName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Annotation
 
value = instance.InsertAnnotationFavorite(BstrFileName, X, Y, Z)
```

```

Annotation InsertAnnotationFavorite( 
   System.string BstrFileName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Annotation^ InsertAnnotationFavorite( 
   System.String^ BstrFileName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*BstrFileName*
:   Path and filename of favorites file

*X*
:   x coordinate where to insert the annotations

*Y*
:   y coordinate where to insert the annotations

*Z*
:   z coordinate where to insert the annotations

#### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
