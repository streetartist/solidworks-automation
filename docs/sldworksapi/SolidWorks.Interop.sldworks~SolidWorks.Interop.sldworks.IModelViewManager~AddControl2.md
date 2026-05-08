# AddControl2 Method (IModelViewManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl2`

Obsolete. Superseded by IModelViewManager::AddControl3.
Obsolete. Superseded by [IModelViewManager::AddControl3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddControl2( _
   ByVal Name As System.String, _
   ByVal ControlName As System.String, _
   ByVal BstrLicKey As System.String _
) As System.Object
```

```

Dim instance As IModelViewManager
Dim Name As System.String
Dim ControlName As System.String
Dim BstrLicKey As System.String
Dim value As System.Object
 
value = instance.AddControl2(Name, ControlName, BstrLicKey)
```

```

System.object AddControl2( 
   System.string Name,
   System.string ControlName,
   System.string BstrLicKey
)
```

```

System.Object^ AddControl2( 
   System.String^ Name,
   System.String^ ControlName,
   System.String^ BstrLicKey
) 
```

#### Parameters

*Name*

*ControlName*

*BstrLicKey*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)
