# GetAttachedEntities Method (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttachedEntities`

Gets the entities to which this block instance is attached.
Gets the entities to which this block instance is attached.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachedEntities( _
   ByRef Entities As System.Object, _
   ByRef EntityTypes As System.Object _
) As System.Boolean
```

```

Dim instance As ISketchBlockInstance
Dim Entities As System.Object
Dim EntityTypes As System.Object
Dim value As System.Boolean
 
value = instance.GetAttachedEntities(Entities, EntityTypes)
```

```

System.bool GetAttachedEntities( 
   out System.object Entities,
   out System.object EntityTypes
)
```

```

System.bool GetAttachedEntities( 
   [Out] System.Object^ Entities,
   [Out] System.Object^ EntityTypes
) 
```

#### Parameters

*Entities*
:   Array of attached entities

*EntityTypes*
:   Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) of the types of attached entities (see **Remarks**)

#### Return Value

True if the entities are retrieved, false if not

Remarks

The arrays returned by this method can contain one or more different object and type.

|  |  |
| --- | --- |
| Possible returned Entities | Possible returned EntityTypes |
| [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) | swSelFACES |
| [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) | swSelEDGES |
| [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) | swSelVERTICES |
| [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) | swSelSKETCHSEGS |
| [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) | swSelSKETCHPOINTS |

A block instance that was inserted with a leader attached to an entity remains attached to that entity even if the leader is hidden. If the leader is shown again later on, the leader still points to the entity and the block instance is still properly associated with the entity.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
