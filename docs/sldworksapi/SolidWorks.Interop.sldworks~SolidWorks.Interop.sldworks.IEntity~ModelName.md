# ModelName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~ModelName`

Gets or sets the standard Parasolid name attribute of the entity.
Gets or sets the standard Parasolid name attribute of the entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ModelName As System.String
```

```

Dim instance As IEntity
Dim value As System.String
 
instance.ModelName = value
 
value = instance.ModelName
```

```

System.string ModelName {get; set;}
```

```

property System.String^ ModelName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Standard Parasolid name attribute

Example

This Visual Basic subroutine shows how to write a Parasolid name attribute to each face in the model.

Private Sub NameAllFaces (ByRef swBody as SldWorks.body2)

> Dim swFace as Sldworks.Face2
>
> Dim swEnt As Sldworks.Entity
>
> Dim Name, RootName As String
>
> Dim Index As Integer
>
> Dim ret as Boolean

> swFace = swBody.GetFirstFace
>
> Index = 0
>
> RootName = "My Face #"
>
> Do While Not swFace is Nothing
>
> > swEnt = swFace
> >
> > Name = RootName + str(Index)
> >
> > swEnt.ModelName = Name
> >
> > Index = Index + 1
> >
> > swFace = swFace.GetNextFace
>
> Loop

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)
