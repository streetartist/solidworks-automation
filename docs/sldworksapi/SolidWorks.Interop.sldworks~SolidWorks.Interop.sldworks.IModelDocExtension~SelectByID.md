# SelectByID Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID`

Obsolete. Superseded by IModelDocExtension::SelectByID2.
Obsolete. Superseded by [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByID( _
   ByVal Name As System.String, _
   ByVal Type As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Callout As Callout _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim Type As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Callout As Callout
Dim value As System.Boolean
 
value = instance.SelectByID(Name, Type, X, Y, Z, Append, Mark, Callout)
```

```

System.bool SelectByID( 
   System.string Name,
   System.string Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout Callout
)
```

```

System.bool SelectByID( 
   System.String^ Name,
   System.String^ Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout^ Callout
) 
```

#### Parameters

*Name*

*Type*

*X*

*Y*

*Z*

*Append*

*Mark*

*Callout*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
