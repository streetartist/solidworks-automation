# ReferenceEntity2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity2`

Gets the specified mate entity in this mate reference.
Gets the specified mate entity in this mate reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceEntity2( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.ReferenceEntity2(Index)
```

```

System.object ReferenceEntity2( 
   System.int Index
) {get;}
```

```

property System.Object^ ReferenceEntity2 {
   System.Object^ get(System.int Index);
}
```

#### Parameters

*Index*
:   Mate reference entity as defined in [swMateReferenceIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

#### Property Value

[IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) (see **Remarks**)

Remarks

Before calling this property, call [IMateReference::ReferenceEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityCount.md) to determine the range of values for Index.

After calling this property, call [IMateReference::ReferenceEntityType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityType.md) to determine which type this property returns and then cast the returned object into the appropriate type.

Example

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)  
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)  
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)  
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.md)
