# Reference Property (IMateEntity2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~Reference`

Gets the mate reference for this mate entity.
Gets the mate reference for this mate entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Reference As System.Object
```

```

Dim instance As IMateEntity2
Dim value As System.Object
 
value = instance.Reference
```

```

System.object Reference {get;}
```

```

property System.Object^ Reference {
   System.Object^ get();
}
```

#### Property Value

[Mate reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)

Remarks

Mate references can be one or more entities of a component used for automatic mating.

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md)  
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.md)  
[IMateEntity2::ReferenceComponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceComponent.md)  
[IMateEntity2::ReferenceType2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceType2.md)
